#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* epsview.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepceps.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsview_ EPSVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsview_ epsview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsviewfromoptions_ EPSVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsviewfromoptions_ epsviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsconvergedreasonview_ EPSCONVERGEDREASONVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsconvergedreasonview_ epsconvergedreasonview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsconvergedreasonviewfromoptions_ EPSCONVERGEDREASONVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsconvergedreasonviewfromoptions_ epsconvergedreasonviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epserrorview_ EPSERRORVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epserrorview_ epserrorview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epserrorviewfromoptions_ EPSERRORVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epserrorviewfromoptions_ epserrorviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsvaluesview_ EPSVALUESVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsvaluesview_ epsvaluesview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsvaluesviewfromoptions_ EPSVALUESVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsvaluesviewfromoptions_ epsvaluesviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsvectorsview_ EPSVECTORSVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsvectorsview_ epsvectorsview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsvectorsviewfromoptions_ EPSVECTORSVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsvectorsviewfromoptions_ epsvectorsviewfromoptions
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  epsview_(EPS eps,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(viewer);
*ierr = EPSView(
	(EPS)PetscToPointer((eps) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  epsviewfromoptions_(EPS eps,PetscObject obj, char name[], int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(obj);
/* insert Fortran-to-C conversion for name */
  FIXCHAR(name,cl0,_cltmp0);
*ierr = EPSViewFromOptions(
	(EPS)PetscToPointer((eps) ),
	(PetscObject)PetscToPointer((obj) ),_cltmp0);
  FREECHAR(name,_cltmp0);
}
SLEPC_EXTERN void  epsconvergedreasonview_(EPS eps,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(viewer);
*ierr = EPSConvergedReasonView(
	(EPS)PetscToPointer((eps) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  epsconvergedreasonviewfromoptions_(EPS eps, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSConvergedReasonViewFromOptions(
	(EPS)PetscToPointer((eps) ));
}
SLEPC_EXTERN void  epserrorview_(EPS eps,EPSErrorType *etype,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(viewer);
*ierr = EPSErrorView(
	(EPS)PetscToPointer((eps) ),*etype,PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  epserrorviewfromoptions_(EPS eps, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSErrorViewFromOptions(
	(EPS)PetscToPointer((eps) ));
}
SLEPC_EXTERN void  epsvaluesview_(EPS eps,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(viewer);
*ierr = EPSValuesView(
	(EPS)PetscToPointer((eps) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  epsvaluesviewfromoptions_(EPS eps, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSValuesViewFromOptions(
	(EPS)PetscToPointer((eps) ));
}
SLEPC_EXTERN void  epsvectorsview_(EPS eps,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(viewer);
*ierr = EPSVectorsView(
	(EPS)PetscToPointer((eps) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  epsvectorsviewfromoptions_(EPS eps, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSVectorsViewFromOptions(
	(EPS)PetscToPointer((eps) ));
}
#if defined(__cplusplus)
}
#endif

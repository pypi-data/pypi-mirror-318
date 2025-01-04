#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* pepview.c */
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

#include "slepcpep.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepview_ PEPVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepview_ pepview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepviewfromoptions_ PEPVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepviewfromoptions_ pepviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepconvergedreasonview_ PEPCONVERGEDREASONVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepconvergedreasonview_ pepconvergedreasonview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepconvergedreasonviewfromoptions_ PEPCONVERGEDREASONVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepconvergedreasonviewfromoptions_ pepconvergedreasonviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define peperrorview_ PEPERRORVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define peperrorview_ peperrorview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define peperrorviewfromoptions_ PEPERRORVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define peperrorviewfromoptions_ peperrorviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepvaluesview_ PEPVALUESVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepvaluesview_ pepvaluesview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepvaluesviewfromoptions_ PEPVALUESVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepvaluesviewfromoptions_ pepvaluesviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepvectorsview_ PEPVECTORSVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepvectorsview_ pepvectorsview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepvectorsviewfromoptions_ PEPVECTORSVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepvectorsviewfromoptions_ pepvectorsviewfromoptions
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  pepview_(PEP pep,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLOBJECT(viewer);
*ierr = PEPView(
	(PEP)PetscToPointer((pep) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  pepviewfromoptions_(PEP pep,PetscObject obj, char name[], int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLOBJECT(obj);
/* insert Fortran-to-C conversion for name */
  FIXCHAR(name,cl0,_cltmp0);
*ierr = PEPViewFromOptions(
	(PEP)PetscToPointer((pep) ),
	(PetscObject)PetscToPointer((obj) ),_cltmp0);
  FREECHAR(name,_cltmp0);
}
SLEPC_EXTERN void  pepconvergedreasonview_(PEP pep,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLOBJECT(viewer);
*ierr = PEPConvergedReasonView(
	(PEP)PetscToPointer((pep) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  pepconvergedreasonviewfromoptions_(PEP pep, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPConvergedReasonViewFromOptions(
	(PEP)PetscToPointer((pep) ));
}
SLEPC_EXTERN void  peperrorview_(PEP pep,PEPErrorType *etype,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLOBJECT(viewer);
*ierr = PEPErrorView(
	(PEP)PetscToPointer((pep) ),*etype,PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  peperrorviewfromoptions_(PEP pep, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPErrorViewFromOptions(
	(PEP)PetscToPointer((pep) ));
}
SLEPC_EXTERN void  pepvaluesview_(PEP pep,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLOBJECT(viewer);
*ierr = PEPValuesView(
	(PEP)PetscToPointer((pep) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  pepvaluesviewfromoptions_(PEP pep, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPValuesViewFromOptions(
	(PEP)PetscToPointer((pep) ));
}
SLEPC_EXTERN void  pepvectorsview_(PEP pep,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLOBJECT(viewer);
*ierr = PEPVectorsView(
	(PEP)PetscToPointer((pep) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  pepvectorsviewfromoptions_(PEP pep, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPVectorsViewFromOptions(
	(PEP)PetscToPointer((pep) ));
}
#if defined(__cplusplus)
}
#endif

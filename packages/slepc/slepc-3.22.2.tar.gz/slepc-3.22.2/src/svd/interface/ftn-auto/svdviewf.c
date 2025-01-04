#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* svdview.c */
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

#include "slepcsvd.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdview_ SVDVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdview_ svdview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdviewfromoptions_ SVDVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdviewfromoptions_ svdviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdconvergedreasonview_ SVDCONVERGEDREASONVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdconvergedreasonview_ svdconvergedreasonview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdconvergedreasonviewfromoptions_ SVDCONVERGEDREASONVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdconvergedreasonviewfromoptions_ svdconvergedreasonviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svderrorview_ SVDERRORVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svderrorview_ svderrorview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svderrorviewfromoptions_ SVDERRORVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svderrorviewfromoptions_ svderrorviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdvaluesview_ SVDVALUESVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdvaluesview_ svdvaluesview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdvaluesviewfromoptions_ SVDVALUESVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdvaluesviewfromoptions_ svdvaluesviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdvectorsview_ SVDVECTORSVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdvectorsview_ svdvectorsview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdvectorsviewfromoptions_ SVDVECTORSVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdvectorsviewfromoptions_ svdvectorsviewfromoptions
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  svdview_(SVD svd,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLOBJECT(viewer);
*ierr = SVDView(
	(SVD)PetscToPointer((svd) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  svdviewfromoptions_(SVD svd,PetscObject obj, char name[], int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLOBJECT(obj);
/* insert Fortran-to-C conversion for name */
  FIXCHAR(name,cl0,_cltmp0);
*ierr = SVDViewFromOptions(
	(SVD)PetscToPointer((svd) ),
	(PetscObject)PetscToPointer((obj) ),_cltmp0);
  FREECHAR(name,_cltmp0);
}
SLEPC_EXTERN void  svdconvergedreasonview_(SVD svd,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLOBJECT(viewer);
*ierr = SVDConvergedReasonView(
	(SVD)PetscToPointer((svd) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  svdconvergedreasonviewfromoptions_(SVD svd, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDConvergedReasonViewFromOptions(
	(SVD)PetscToPointer((svd) ));
}
SLEPC_EXTERN void  svderrorview_(SVD svd,SVDErrorType *etype,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLOBJECT(viewer);
*ierr = SVDErrorView(
	(SVD)PetscToPointer((svd) ),*etype,PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  svderrorviewfromoptions_(SVD svd, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDErrorViewFromOptions(
	(SVD)PetscToPointer((svd) ));
}
SLEPC_EXTERN void  svdvaluesview_(SVD svd,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLOBJECT(viewer);
*ierr = SVDValuesView(
	(SVD)PetscToPointer((svd) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  svdvaluesviewfromoptions_(SVD svd, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDValuesViewFromOptions(
	(SVD)PetscToPointer((svd) ));
}
SLEPC_EXTERN void  svdvectorsview_(SVD svd,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLOBJECT(viewer);
*ierr = SVDVectorsView(
	(SVD)PetscToPointer((svd) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  svdvectorsviewfromoptions_(SVD svd, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDVectorsViewFromOptions(
	(SVD)PetscToPointer((svd) ));
}
#if defined(__cplusplus)
}
#endif

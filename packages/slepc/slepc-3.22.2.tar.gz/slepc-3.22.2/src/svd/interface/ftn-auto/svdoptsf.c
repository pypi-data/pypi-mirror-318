#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* svdopts.c */
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
#define svdsetimplicittranspose_ SVDSETIMPLICITTRANSPOSE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetimplicittranspose_ svdsetimplicittranspose
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgetimplicittranspose_ SVDGETIMPLICITTRANSPOSE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgetimplicittranspose_ svdgetimplicittranspose
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsettolerances_ SVDSETTOLERANCES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsettolerances_ svdsettolerances
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgettolerances_ SVDGETTOLERANCES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgettolerances_ svdgettolerances
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsetdimensions_ SVDSETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetdimensions_ svdsetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgetdimensions_ SVDGETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgetdimensions_ svdgetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsetwhichsingulartriplets_ SVDSETWHICHSINGULARTRIPLETS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetwhichsingulartriplets_ svdsetwhichsingulartriplets
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgetwhichsingulartriplets_ SVDGETWHICHSINGULARTRIPLETS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgetwhichsingulartriplets_ svdgetwhichsingulartriplets
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsetconvergencetest_ SVDSETCONVERGENCETEST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetconvergencetest_ svdsetconvergencetest
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgetconvergencetest_ SVDGETCONVERGENCETEST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgetconvergencetest_ svdgetconvergencetest
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsetstoppingtest_ SVDSETSTOPPINGTEST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetstoppingtest_ svdsetstoppingtest
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgetstoppingtest_ SVDGETSTOPPINGTEST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgetstoppingtest_ svdgetstoppingtest
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsetfromoptions_ SVDSETFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetfromoptions_ svdsetfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsetproblemtype_ SVDSETPROBLEMTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetproblemtype_ svdsetproblemtype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgetproblemtype_ SVDGETPROBLEMTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgetproblemtype_ svdgetproblemtype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdisgeneralized_ SVDISGENERALIZED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdisgeneralized_ svdisgeneralized
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdishyperbolic_ SVDISHYPERBOLIC
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdishyperbolic_ svdishyperbolic
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsettrackall_ SVDSETTRACKALL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsettrackall_ svdsettrackall
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgettrackall_ SVDGETTRACKALL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgettrackall_ svdgettrackall
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsetoptionsprefix_ SVDSETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetoptionsprefix_ svdsetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdappendoptionsprefix_ SVDAPPENDOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdappendoptionsprefix_ svdappendoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgetoptionsprefix_ SVDGETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgetoptionsprefix_ svdgetoptionsprefix
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  svdsetimplicittranspose_(SVD svd,PetscBool *impl, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDSetImplicitTranspose(
	(SVD)PetscToPointer((svd) ),*impl);
}
SLEPC_EXTERN void  svdgetimplicittranspose_(SVD svd,PetscBool *impl, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDGetImplicitTranspose(
	(SVD)PetscToPointer((svd) ),impl);
}
SLEPC_EXTERN void  svdsettolerances_(SVD svd,PetscReal *tol,PetscInt *maxits, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDSetTolerances(
	(SVD)PetscToPointer((svd) ),*tol,*maxits);
}
SLEPC_EXTERN void  svdgettolerances_(SVD svd,PetscReal *tol,PetscInt *maxits, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLREAL(tol);
CHKFORTRANNULLINTEGER(maxits);
*ierr = SVDGetTolerances(
	(SVD)PetscToPointer((svd) ),tol,maxits);
}
SLEPC_EXTERN void  svdsetdimensions_(SVD svd,PetscInt *nsv,PetscInt *ncv,PetscInt *mpd, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDSetDimensions(
	(SVD)PetscToPointer((svd) ),*nsv,*ncv,*mpd);
}
SLEPC_EXTERN void  svdgetdimensions_(SVD svd,PetscInt *nsv,PetscInt *ncv,PetscInt *mpd, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLINTEGER(nsv);
CHKFORTRANNULLINTEGER(ncv);
CHKFORTRANNULLINTEGER(mpd);
*ierr = SVDGetDimensions(
	(SVD)PetscToPointer((svd) ),nsv,ncv,mpd);
}
SLEPC_EXTERN void  svdsetwhichsingulartriplets_(SVD svd,SVDWhich *which, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDSetWhichSingularTriplets(
	(SVD)PetscToPointer((svd) ),*which);
}
SLEPC_EXTERN void  svdgetwhichsingulartriplets_(SVD svd,SVDWhich *which, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDGetWhichSingularTriplets(
	(SVD)PetscToPointer((svd) ),which);
}
SLEPC_EXTERN void  svdsetconvergencetest_(SVD svd,SVDConv *conv, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDSetConvergenceTest(
	(SVD)PetscToPointer((svd) ),*conv);
}
SLEPC_EXTERN void  svdgetconvergencetest_(SVD svd,SVDConv *conv, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDGetConvergenceTest(
	(SVD)PetscToPointer((svd) ),conv);
}
SLEPC_EXTERN void  svdsetstoppingtest_(SVD svd,SVDStop *stop, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDSetStoppingTest(
	(SVD)PetscToPointer((svd) ),*stop);
}
SLEPC_EXTERN void  svdgetstoppingtest_(SVD svd,SVDStop *stop, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDGetStoppingTest(
	(SVD)PetscToPointer((svd) ),stop);
}
SLEPC_EXTERN void  svdsetfromoptions_(SVD svd, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDSetFromOptions(
	(SVD)PetscToPointer((svd) ));
}
SLEPC_EXTERN void  svdsetproblemtype_(SVD svd,SVDProblemType *type, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDSetProblemType(
	(SVD)PetscToPointer((svd) ),*type);
}
SLEPC_EXTERN void  svdgetproblemtype_(SVD svd,SVDProblemType *type, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDGetProblemType(
	(SVD)PetscToPointer((svd) ),type);
}
SLEPC_EXTERN void  svdisgeneralized_(SVD svd,PetscBool* is, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDIsGeneralized(
	(SVD)PetscToPointer((svd) ),is);
}
SLEPC_EXTERN void  svdishyperbolic_(SVD svd,PetscBool* is, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDIsHyperbolic(
	(SVD)PetscToPointer((svd) ),is);
}
SLEPC_EXTERN void  svdsettrackall_(SVD svd,PetscBool *trackall, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDSetTrackAll(
	(SVD)PetscToPointer((svd) ),*trackall);
}
SLEPC_EXTERN void  svdgettrackall_(SVD svd,PetscBool *trackall, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDGetTrackAll(
	(SVD)PetscToPointer((svd) ),trackall);
}
SLEPC_EXTERN void  svdsetoptionsprefix_(SVD svd, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(svd);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = SVDSetOptionsPrefix(
	(SVD)PetscToPointer((svd) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  svdappendoptionsprefix_(SVD svd, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(svd);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = SVDAppendOptionsPrefix(
	(SVD)PetscToPointer((svd) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  svdgetoptionsprefix_(SVD svd, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDGetOptionsPrefix(
	(SVD)PetscToPointer((svd) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for prefix */
*ierr = PetscStrncpy(prefix, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, prefix, cl0);
}
#if defined(__cplusplus)
}
#endif
